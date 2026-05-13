class Solution {
public:
    double myPow(double x, int n) {
        long long N = n; // Handle INT_MIN overflow
        if (N < 0) {
            return 1.0 / solve(x, -N);
        }
        return solve(x, N);
    }

private:
    double solve(double x, long long n) {
        if (n == 0) return 1.0;

        double half = solve(x, n / 2);

        if (n % 2 == 0) {
            return half * half;
        } else {
            return half * half * x;
        }
    }
};