const Navbar = ({ selectedLink, setSelectedLink }) => {
  return (
    <div className="w-full h-24 bg-cyan-900 relative flex items-center">
      <div className="ml-5 text-white text-4xl font-normal">FOCUSED</div>
      <div
        className="ml-52 text-white text-2xl font-normal hover:cursor-pointer relative"
        onClick={() => setSelectedLink("home")}
      >
        HOME
        {selectedLink === "home" && (
          <span className="absolute -bottom-1 left-0 w-full h-1 bg-white" />
        )}
      </div>
      <div
        className="ml-10 text-white text-2xl font-normal hover:cursor-pointer relative"
        onClick={() => setSelectedLink("dashboard")}
      >
        DASHBOARD
        {selectedLink === "dashboard" && (
          <span className="absolute -bottom-1 left-0 w-full h-1 bg-white" />
        )}
      </div>

      <div className="right-5 absolute">
        <input
          className="w-64 h-11 rounded-3xl pl-5 pr-5 py-2 text-black text-1xl font-normal bg-white"
          type="text"
          placeholder="Search"
          onChange={(e) => console.log(e.target.value)}
        />
      </div>
    </div>
  );
};

export default Navbar;
