import React from "react";

const Tab = ({ title, selected, onSelect }) => {
  return (
    <div
      className={`w-56 h-16 ml-4 rounded-2xl ${
        selected ? "bg-cyan-600 bg-opacity-50 translate-z-10 shadow-lg" : ""
      } flex justify-center items-center cursor-pointer`}
      onClick={() => onSelect(title)}
    >
      <div
        className={`text-2xl font-normal uppercase ${
          selected ? "text-white" : "text-black"
        }`}
      >
        {title}
      </div>
    </div>
  );
};

export default Tab;
