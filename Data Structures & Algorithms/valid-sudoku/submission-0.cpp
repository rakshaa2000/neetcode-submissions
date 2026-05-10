class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, unordered_set<int>> rows, cols, boxes;
        for (int i=0; i<9; i++){
            for (int j=0; j<9; j++){
                if (board[i][j] == '.') continue;
                int num = board[i][j] - '0';
                if (rows[i].count(num) || cols[j].count(num) || boxes[i/3 *3 + j/3].count(num)) return false;
                rows[i].insert(num);
                cols[j].insert(num);
                boxes[i/3*3 + j/3].insert(num);
            }
        }
        return true;
    }
};
