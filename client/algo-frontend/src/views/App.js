import React from "react";
import { useEffect, useState } from "react";
import BacktestChart from "./components/BacktestChart";
import BacktestController from "./controllers/BacktestController";

const App = () => {
  const [backtestData, setBacktestData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const data = await BacktestController.fetchBacktestData();
      setBacktestData(data);
    };

    fetchData();
  }, []);

  return (
    <div className="App">
      <h1>Backtest Visualizer</h1>
      {backtestData.length > 0 ? (
        <BacktestChart data={backtestData} />
      ) : (
        <p> Loading backtest data...</p>
      )}
    </div>
  );
};

export default App;