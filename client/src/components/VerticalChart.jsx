// App.js
import Chart from "chart.js/auto";
import {
  CategoryScale,
  LinearScale,
  BarController,
  BarElement,
} from "chart.js";
import { BarChart } from "./BarChart";

Chart.register(CategoryScale, LinearScale, BarController, BarElement);

export default function VerticalChart({ data }) {
  const chartData = {
    labels: data.map((data) => data.name),
    datasets: [
      {
        label: "Percentage of companies using this package",
        data: data.map((data) => data.count),
        backgroundColor: [
          "rgba(243, 156, 18, 1)", // orange color
          "#27ae60",
          "rgba(75, 192, 192, 1)", // teal color
          "rgba(255, 99, 132, 1)", // pink color
          "#1abc9c", // turquoise color
          "#e74c3c", // tomato red color
          "#8e44ad", // wisteria color
          "#2980b9", // belize hole blue color
          "#f39c12", // sunflower yellow color
          "#16a085", // dark green color
          "#e67e22", // carrot orange color
          "#d35400", // pumpkin color
          "#c0392b", // pomegranate red color
          "#2c3e50",
        ],

        borderWidth: 0, // Set the border width to 0
        borderRadius: 10, // Set the border radius for rounded corners
      },
    ],
  };

  const options = {
    plugins: {
      title: {
        display: true,
        color: "white",
      },
      legend: {
        display: false,
      },
    },
  };

  return (
    <div className="mt-5">
      <BarChart chartData={chartData} options={options} />
    </div>
  );
}
