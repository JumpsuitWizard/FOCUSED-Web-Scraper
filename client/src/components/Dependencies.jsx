import { useState } from "react";
import { FaArrowDown } from "react-icons/fa";
import { Badges } from "./Companies";

const Dependencies = ({ data }) => {
  const [visibleItems, setVisibleItems] = useState(6);
  const itemsPerPage = 6;
  const totalItems = data.length;

  const handleViewMore = () => {
    setVisibleItems((prevVisibleItems) => prevVisibleItems + itemsPerPage);
  };
  return (
    <>
      <div className="mt-14 grid grid-cols-3 gap-4 mx-4 my-4 gap-y-12">
        {data.slice(0, visibleItems).map((value) => (
          <div
            key={value.index}
            className="w-96 bg-zinc-100 rounded-lg p-6 relative translate-z-10 shadow-md"
          >
            <div className="w-96 h-12 text-black text-opacity-70 text-xl absolute top-0 left-0 font-bold bg-cyan-600 bg-opacity-50 rounded-t-lg flex items-center pl-4">
              {value.name}
            </div>
            <div className="w-96 h-10 mt-10 text-black text-xl font-bold">
              Companies sharing{" "}
              {value.name.slice(0, 12) + (value.name.length > 14 ? "..." : "")}
            </div>
            <div
              className="flex gap-2 flex-wrap"
              style={{ maxHeight: "11rem", overflowY: "auto" }}
            >
              {value.shared_authors.map((value) => (
                <Badges key={value} text={value.toLowerCase()} type="company" />
              ))}
            </div>
          </div>
        ))}
      </div>
      <div className="mt-7 pb-4 absolute left-1/2 transform -translate-y-1/2">
        {visibleItems < totalItems && (
          <button className="flex items-center" onClick={handleViewMore}>
            View More <FaArrowDown className="ml-2" />
          </button>
        )}
      </div>
    </>
  );
};

export default Dependencies;
