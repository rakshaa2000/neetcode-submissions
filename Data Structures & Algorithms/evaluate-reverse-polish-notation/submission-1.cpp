class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> num;
        for (auto& token : tokens){
            if (token == "+" || token == "-" || token == "*" || token == "/"){
                int num2 = num.top();
                num.pop();
                int num1 = num.top();
                num.pop();
                char op = token[0];
                switch(op){
                    case '+': {
                        num.push(num1 + num2);
                        break;
                    }
                    case '-': {
                        num.push(num1 - num2);
                        break;
                    }
                    case '/': {
                        num.push(num1 / num2);
                        break;
                    }
                    case '*': {
                        num.push(num1 * num2);
                        break;
                    }
                }
            }
            else{
                num.push(stoi(token));
            }
        }
        return num.top();
    }
};
