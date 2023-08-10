// App.js
import Chart from "chart.js/auto";
import {
  CategoryScale,
  LinearScale,
  BarController,
  BarElement,
} from "chart.js";
import { BarChart } from "./BarChart";
import ChartDataLabels from "chartjs-plugin-datalabels";

Chart.register(
  CategoryScale,
  LinearScale,
  BarController,
  BarElement,
  ChartDataLabels
);

export default function DashboardChart({ data }) {
  const chartData = {
    labels: data.map((data) => data.name),
    plugins: [ChartDataLabels],
    datasets: [
      {
        label: "Count",
        data: data.map((data) => data.count),
        backgroundColor: [
          // green color
          "#f3ba2f", // yellow color
          "#2a71d0", // blue color
          "rgba(221, 76, 57, 1)", // red color
          "#9b59b6", // purple color
          "#3498db", // dark blue color
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
          "#2c3e50", // midnight blue color
        ],

        borderWidth: 0, // Set the border width to 0
        borderRadius: 10, // Set the border radius for rounded corners
        barThickness: 13, // Set the width of each bar in pixels
      },
    ],
  };

  const options = {
    indexAxis: "y", // This option sets the axis to be horizontal
    scales: {
      x: {
        display: false, // Hide x-axis
        beginAtZero: true,
        grid: {
          display: false, // Remove the grid lines for the x-axis
        },
      },
      y: {
        beginAtZero: true,
        grid: {
          display: false, // Remove the grid lines for the y-axis
        },
      },
    },
    plugins: {
      title: {
        display: true,
      },
      legend: {
        display: false,
      },
      datalabels: {
        anchor: "end",
        align: "end",
        offset: 3,
        font: {
          size: 12,
        },
        color: "#000",
      },
    },
  };

  return (
    <div className="mt-5">
      <BarChart chartData={chartData} options={options} />
    </div>
  );
}
