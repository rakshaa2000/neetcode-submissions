class Solution {
public:
    bool canEat(vector<int> piles, int speed, int hours){
        long long h = 0;
        for (auto& pile : piles){
            h += (pile + speed - 1) / speed;
        }
        return h <= hours;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1, right = *max_element(piles.begin(), piles.end());
        int lowest = right;
        while (left <= right){
            int mid = left + (right - left )/ 2;
            if (canEat(piles, mid, h)){
                lowest = mid;
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        return lowest;
    }
};
