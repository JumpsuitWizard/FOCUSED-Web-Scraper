// components/BarChart.js
import { Bar } from "react-chartjs-2";
export const BarChart = ({ chartData, options }) => {
  return <Bar data={chartData} options={options} />;
};
