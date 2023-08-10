import React, { useEffect, useState } from "react";
const Modal = ({ isOpen, onClose, text, type }) => {
  const [data, setData] = useState(null);
  useEffect(() => {
    const fetchData = async () => {
      try {
        if (type === "package") {
          const response = await fetch(
            `http://127.0.0.1:4000/dependencies/package/${text}`
          );

          const data = await response.json();

          const transformedData = new Set(
            data.components.map((value) => value.company.name)
          );
          setData([...transformedData]);
        } else if (type === "company") {
          const response = await fetch(
            `http://127.0.0.1:4000/dependencies/company/${text}`
          );
          const data = await response.json();

          const transformedData = new Set(
            data.components.map((value) => value.name)
          );
          setData([...transformedData]);
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, [type, text, isOpen]);
  return (
    <>
      {isOpen && (
        <>
          <div className="fixed top-0 left-0 w-full h-full bg-black opacity-70 z-40"></div>
          <div className="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-modal-overlay z-50">
            <div
              key="1"
              className="w-96 bg-zinc-100 rounded-lg p-6 relative translate-z-10 shadow-md"
            >
              <div className="w-96 h-12 text-black text-opacity-70 text-xl absolute top-0 left-0 font-bold bg-cyan-600 bg-opacity-50 rounded-t-lg flex items-center pl-4">
                {text}
                <button
                  onClick={onClose}
                  className="text-gray-700 absolute right-3 hover:text-gray-900 focus:outline-none"
                >
                  <svg
                    className="w-6 h-6"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M6 18L18 6M6 6l12 12"
                    />
                  </svg>
                </button>
              </div>
              <div className="w-96 h-10 mt-10 text-black text-xl font-bold">
                {type === "company" ? "Dependencies" : "Shared by companies"}
              </div>
              <div
                className="flex gap-2 flex-wrap"
                style={{ maxHeight: "8rem", overflowY: "auto" }}
              >
                {data === null ? (
                  <p>Loading...</p>
                ) : data.length === 0 ? (
                  <p>No data available</p>
                ) : (
                  data.map((value) => (
                    <Badges key={value} text={value.toLowerCase()} />
                  ))
                )}
              </div>
            </div>
          </div>
        </>
      )}
    </>
  );
};
export const Badges = ({ text }) => {
  return (
    <div className="inline-block rounded-lg border border-neutral-400 px-2 py-1 cursor-pointer">
      <div className="text-blue-950 text-base font-medium">{text}</div>
    </div>
  );
};

export default Modal;
