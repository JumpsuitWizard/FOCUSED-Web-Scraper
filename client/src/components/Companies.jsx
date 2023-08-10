import { FaArrowRightLong } from "react-icons/fa6";
import { GoLink } from "react-icons/go";
import { Link } from "react-router-dom";
import Modal from "./Popup";
import { useState } from "react";
import { links } from "./data";

const Companies = ({ data }) => {
  const getURL = (name) => {
    const formattedName = name.replace(/\s+/g, "_").toLowerCase();
    const matchingKey = Object.keys(links).find((key) =>
      key.toLowerCase().includes(formattedName)
    );
    return matchingKey ? links[matchingKey] : null;
  };

  return (
    <div className="mt-14 grid grid-cols-3 gap-4 gap-y-12">
      {data.map((company) => (
        <div
          key={company.index}
          className="w-96 h-80 bg-zinc-100 rounded-lg p-6 relative translate-z-10 shadow-md"
        >
          <div className="w-96 h-12 text-black text-opacity-70 text-xl absolute top-0 left-0 font-bold bg-cyan-600 bg-opacity-50 rounded-t-lg flex items-center pl-4">
            {company.company_name
              .toLowerCase()
              .replace(/\b\w/g, (l) => l.toUpperCase())}
          </div>
          <div className="mt-10 cursor-pointer">
            <button
              onClick={() => {
                const url = getURL(company.company_name);
                if (url) {
                  window.open(url, "_blank");
                }
              }}
              key="Company Link"
              className="inline-flex items-center py-1 cursor-pointer text-base font-medium hover:text-cyan-600"
            >
              Company Link
              <GoLink className="ml-2" />
            </button>
          </div>
          <div className="w-96 h-10 mt-2 text-black text-xl font-bold">
            Dependencies
          </div>
          <div
            className="flex gap-2 flex-wrap"
            style={{ maxHeight: "8rem", overflowY: "auto" }}
          >
            {[...new Set(company.packages)].map((value) => (
              <Badges key={value} text={value.toLowerCase()} type="package" />
            ))}
          </div>
          <Link
            to={`/company/${company.company_name}`}
            className="absolute bottom-3 right-6 cursor-pointer transition-transform duration-300 ease-in-out transform hover:scale-125 hover:translate-x-1"
          >
            <FaArrowRightLong size={24} />
          </Link>
        </div>
      ))}
    </div>
  );
};

export const Badges = ({ text, type, highlight }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const handleOpenModal = () => {
    if (!isModalOpen) setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
  };
  return (
    <div
      className={`inline-block rounded-lg border border-neutral-400 px-2 py-1 cursor-pointer ${
        highlight ? "bg-cyan-600 bg-opacity-50" : ""
      } hover:bg-cyan-600 hover:bg-opacity-50`}
    >
      <div
        className="text-blue-950 text-base font-medium "
        onClick={handleOpenModal}
      >
        {text}
      </div>
      {isModalOpen && (
        <Modal
          isOpen={isModalOpen}
          onClose={handleCloseModal}
          text={text}
          type={type}
        />
      )}
    </div>
  );
};

export default Companies;
