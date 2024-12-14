class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prereq) {
        vector<vector<int>> graph(numCourses);
        vector<int> indegree(numCourses);
        vector<int> ans;
        for(int i=0;i<prereq.size();i++){
            graph[prereq[i][0]].push_back(prereq[i][1]);
            indegree[prereq[i][1]]++;
        }
        
        stack<int> nodesWithDegreeZero;
        int count=0;
        
        for(int i=0;i<indegree.size();i++){
            if(indegree[i]==0){
                nodesWithDegreeZero.push(i);
            }
        }
        while(!nodesWithDegreeZero.empty()){
            int curr=nodesWithDegreeZero.top();
            nodesWithDegreeZero.pop();
            count++;
            ans.insert(ans.begin(),curr);
            for(int i=0;i<graph[curr].size();i++){
                if(--indegree[graph[curr][i]]==0){
                    nodesWithDegreeZero.push(graph[curr][i]);
                }
            }
        }
        if(count!=numCourses){
            vector<int> tempans;
            return tempans;
        }
        return ans;
    }
};
