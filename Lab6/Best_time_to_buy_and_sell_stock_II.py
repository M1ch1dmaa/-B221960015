class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n= prices.size();
        int profit = 0;
        // take into profit only those days for which the next day's price is greater.
        for(int day=1;day<n;day++){
            if(prices[day]>prices[day-1]){
                profit +=(prices[day] - prices[day-1]);
            }
        }
        return profit;
    }
};
