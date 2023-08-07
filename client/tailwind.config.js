/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      height: {
        '100': '30rem',
        '110' : '37rem'
        // Add more custom height classes as needed
      },
      width: {
        '100': '30rem',
        '110' : '37rem'
        // Add more custom width classes as needed
      },
    },
  },
  plugins: [],
}