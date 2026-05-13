class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int>& A = nums1;
        vector<int>& B = nums2;
        int total = A.size() + B.size(), half = (total + 1) / 2;
        if (B.size() < A.size()) swap(A, B);
        int left = 0, right = A.size();
        while (left <= right){
            int i = left + (right - left)/2;
            int j = half - i;
            int A_left = i > 0 ? A[i-1] : INT_MIN;
            int A_right = i < A.size() ? A[i] : INT_MAX;
            int B_left = j > 0 ? B[j-1] : INT_MIN;
            int B_right = j < B.size() ? B[j] : INT_MAX;

            if (A_left <= B_right && B_left <= A_right){
                if (total % 2 == 0){
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2.0;
                }
                else{
                    return max(A_left, B_left);
                }
            }
            else if (A_left > B_right){
                right = i-1;
            }
            else{
                left = i+1;
            }
        }
        return -1;
    }
};
