class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for (auto& ch : s){
            if (ch == '(' || ch == '{' || ch == '[') stk.push(ch);
            else if (stk.empty() || ((ch == ')' && stk.top() != '(') || (ch == '}' && stk.top() != '{') || (ch == ']' && stk.top() != '[')))  return false;
            else stk.pop();
        }
        return stk.empty();
    }
};
