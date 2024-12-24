// FaceAuthentication.jsx

import React, { useEffect, useState, useRef } from "react";
import axios from "axios";
import * as tmImage from "@teachablemachine/image";
import styles from "./FaceAuthentication.module.css"; // Import CSS module

const FaceAuthentication = ({ isCheckIn }) => {
  const [model, setModel] = useState(null);
  const [label, setLabel] = useState("");
  const [dataPreview, setDataPreview] = useState("No data yet");
  const [error, setError] = useState(null); 
  const [showToast, setShowToast] = useState(false); 
  const [toastMessage, setToastMessage] = useState("");
  const [toastType, setToastType] = useState("success"); 

  
  const lastSentIds = useRef([]); 
  const detectionTimeout = useRef(null);
  const lastSentMaNV = useRef(null); 
  const webcamRef = useRef(null);
  const webcamInstance = useRef(null); 

  const URL = "https://teachablemachine.withgoogle.com/models/onyHyFuNk/";
  const apiEndpoint = "http://localhost:5000/api/bangchamcong/insert"; // 3000

  useEffect(() => {
    let isMounted = true; 

    const loadModel = async () => {
      try {
        const modelURL = URL + "model.json";
        const metadataURL = URL + "metadata.json";
        const loadedModel = await tmImage.load(modelURL, metadataURL);

        const newWebcam = new tmImage.Webcam(600, 600, true);
        await newWebcam.setup(); 
        await newWebcam.play();

        // if (isMounted && webcamRef.current) {
        //   webcamRef.current.appendChild(newWebcam.canvas);
        // }
        //check xem co them camera khong

        webcamInstance.current = newWebcam;
        setModel(loadedModel);

         loop(newWebcam, loadedModel);
      } catch (err) {
        console.error("Failed to load model or setup webcam:", err);
        setError("Cannot access webcam. Please check your permissions.");
        showCustomToast("Cannot access webcam. Please check your permissions.", "error");
      }
    };

    loadModel();

    return () => {
      isMounted = false;
      // Clean up the webcam stream
      if (webcamInstance.current) {
        webcamInstance.current.stop();
      }
      clearTimeout(detectionTimeout.current);
    };
  }, []);

  const loop = async (webcam, model) => {
    try {
      webcam.update();
      await predict(webcam, model);
      requestAnimationFrame(() => loop(webcam, model));
    } catch (err) {
      console.error("Error in loop:", err);
    }
  };

  const predict = async (webcam, model) => {
    try {
      const prediction = await model.predict(webcam.canvas);

      // Find the prediction with the highest probability
      let highestPrediction = prediction[0];
      for (let i = 1; i < prediction.length; i++) {
        if (prediction[i].probability > highestPrediction.probability) {
          highestPrediction = prediction[i];
        }
      }

      setLabel(`${highestPrediction.className}: ${(highestPrediction.probability * 100).toFixed(2)}%`);

      // If probability > 80% and not sent before
      if (highestPrediction.probability > 0.8) {
        if (!lastSentIds.current.includes(highestPrediction.className)) {
          if (!detectionTimeout.current) {
            detectionTimeout.current = setTimeout(() => {
              sendData(highestPrediction.className);
              detectionTimeout.current = null;
            }, 2000); // Wait 2 seconds before sending
          }
        }
      } else {
        clearTimeout(detectionTimeout.current);
        detectionTimeout.current = null;
      }
    } catch (err) {
      console.error("Error during prediction:", err);
    }
  };

  const sendData = async (className) => {
    const checkValue = isCheckIn ? "checkin" : "checkout";

    const currentTime = new Date();
    const date = currentTime.toISOString().split("T")[0];
    const time = currentTime.toTimeString().split(" ")[0];

    // Validate MaNV
    if (className && className !== "0" && className !== "null") {
      // Prevent sending the same MaNV consecutively
      if (className === lastSentMaNV.current) {
        console.log(`MaNV ${className} has been sent recently, not sending again.`);
        return;
      }

      const payload = {
        MaNV: className,
        TinhTrang: checkValue,
        Ngay: date,
        Gio: time,
      };

      setDataPreview(JSON.stringify(payload, null, 2));

      try {
        const response = await axios.post(apiEndpoint, payload);
        // Show a success message
        showCustomToast("Data has been successfully sent!", "success");

        // Update last sent MaNV
        lastSentMaNV.current = className;

        // Add MaNV to the sent list and maintain a maximum of 5 entries
        lastSentIds.current.push(className);
        if (lastSentIds.current.length > 5) {
          lastSentIds.current.shift();
        }
      } catch (error) {
        console.error("Error while sending data:", error);
        showCustomToast("Failed to send data. Please try again.", "error");
      }
    } else {
      console.warn("Invalid MaNV:", className);
    }
  };

  // Function to display toast
  const showCustomToast = (message, type) => {
    setToastMessage(message);
    setToastType(type);
    setShowToast(true);

    // Automatically hide toast after 3 seconds
    setTimeout(() => {
      setShowToast(false);
    }, 3000);
  };

  return (
    <div className={styles.container}>
      <div className={styles.title}>{isCheckIn ? "Check-In" : "Check-Out"}</div>

      {/* Webcam Section */}
      <div className={styles.webcamContainer} ref={webcamRef}>
        {!webcamInstance.current && !error && (
          <div className={styles.loadingSpinner}>
            <div className="spinner"></div>
          </div>
        )}
        {error && <div className={styles.errorMessage}>{error}</div>}
      </div>

      {/* Prediction Label */}
      <div className={styles.labelDisplay}>{label}</div>

      {/* Data Preview */}
      <div className={styles.dataPreview}>
        <h4>Data to be Sent:</h4>
        <pre>{dataPreview}</pre>
      </div>

      {/* Toast Notification */}
      {showToast && (
        <div className={styles.toastContainer}>
          <div className={`${styles.toast} ${toastType === "error" ? styles.toastError : ""}`}>
            <span>{toastMessage}</span>
            <button className={styles.closeButton} onClick={() => setShowToast(false)}>
              &times;
            </button>
          </div>
        </div>
      )}

      {/* Custom Styles for Spinner */}
      <style jsx>{`
        /* Spinner styling */
        .spinner {
          border: 4px solid #f3f3f3;
          border-top: 4px solid #3498db;
          border-radius: 50%;
          width: 30px;
          height: 30px;
          animation: spin 1s linear infinite;
        }

        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  );
};

export default FaceAuthentication;
