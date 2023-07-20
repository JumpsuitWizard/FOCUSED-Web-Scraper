import React from "react";

const Tab = ({ title, selected, onSelect }) => {
  return (
    <div
      className={`w-56 h-16 ml-4 bg-white rounded-3xl ${
        selected ? "border border-blue-950" : ""
      } flex justify-center items-center cursor-pointer`}
      onClick={() => onSelect(title)}
    >
      <div className={`text-black text-2xl font-normal uppercase`}>{title}</div>
    </div>
  );
};

export default Tab;
