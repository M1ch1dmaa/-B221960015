class MyStack {
public:
    queue<int> q1;
    queue<int> q2;
    
    MyStack() {
        
    }
    
    void push(int x) {
        q1.push(x);     
    }
    
    int pop() {
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }

        int topElement = q1.front();
        q1.pop();

        // Swap q1 and q2
        swap(q1, q2);

        return topElement;                
    }
    
    int top() {
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }

        // The last element in q1 is the top of the stack
        int topElement = q1.front();

        // Push the last element back into q2
        q2.push(q1.front());
        q1.pop();

        // Swap q1 and q2
        swap(q1, q2);

        return topElement;        
    }
    
    bool empty() {
        return q1.empty();        
    }
};
