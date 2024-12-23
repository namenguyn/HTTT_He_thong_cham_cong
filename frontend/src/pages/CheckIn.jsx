// CheckIn.jsx

import React from "react";
import FaceAuthentication from './FaceVerify'

const CheckIn = () => {
  return <FaceAuthentication isCheckIn={true} />;
};

export default CheckIn;
