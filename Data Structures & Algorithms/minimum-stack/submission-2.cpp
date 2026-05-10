class MinStack {
public:
    stack<int> stk, minStack;
    MinStack() {
        
    }
    
    void push(int val) {
        stk.push(val);
        val = min(val, minStack.empty() ? val : minStack.top());
        minStack.push(val);
    }
    
    void pop() {
        stk.pop();
        minStack.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};
