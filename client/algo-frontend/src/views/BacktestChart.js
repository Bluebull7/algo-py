/*
DEPRECATED
SWITCH TO MVC */

import React from 'react';
import { Line } from 'react-chartjs-2';

const BacktestChart = ({ data }) => {
	const chartData = {
		labels: data.map(entry => entry.date),
		datasets: [
			{
				label: 'Portfolio Value',
				data: data.map(entry => entry.portfolioValue),
				borderColor: 'rgba(75,192,192,1)',
				borderWidth: 2,
				fill: false,
			},
		],
	};

const options = {
	scales: {
		x: {
			type: 'time',
			time: {
			  unit: 'day',
			},
		},
		y: {
			beginAtZero: true,
		},
	},
};
return <Line data={chartData} options={options}/>;
};
export default BacktestChart;


