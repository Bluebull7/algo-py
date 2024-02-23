import axios from 'axios'
import BacktestModel from '../models/BacktestModel';

class BacktestController {
    async fetchBacktestData() {
      try {
        const response = await axios.get('http://backend-api/backtest-data');
        return response.data.map(entry => new BacktestModel(entry.date,
    entry.portfolioValue));
      }
    catch(error) {
        console.error('Error fetching backtest data', error);
        return[];
        }
    }
}

export default new BacktestController();
