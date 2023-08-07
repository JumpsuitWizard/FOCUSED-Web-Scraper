import React from "react";
import { FallingLines } from "react-loader-spinner";

const Loader = () => {
  return (
    <div className="h-110 flex flex-col items-center justify-center">
      <FallingLines
        color="#2C9DC2"
        width="100"
        visible={true}
        ariaLabel="falling-lines-loading"
      />
    </div>
  );
};

export default Loader;
