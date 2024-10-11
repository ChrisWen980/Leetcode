class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        ArrayList<ArrayList<Integer>> adj = new ArrayList();

        for(int i = 0; i < numCourses; i++) {
            adj.add(new ArrayList<>());
        }

        for(int i = 0; i < prerequisites.length; i++) {
            adj.get(prerequisites[i][0]).add(prerequisites[i][1]);
        }

        int[] indegrees = new int[numCourses];
        for(int i = 0; i < numCourses; i++) {
            for(int course: adj.get(i)) {
                indegrees[course] += 1;
            }
        }

        Queue<Integer> q = new ArrayDeque<Integer>();
        ArrayList<Integer> processed = new ArrayList<>();
        for(int i = 0; i < numCourses; i++) {
            if(indegrees[i] == 0) {
                q.add(i);
            }
        }

        while(!q.isEmpty()) {
            int root = q.poll();
            processed.add(root);
            for(int course: adj.get(root)) {
                indegrees[course] -= 1;
                if(indegrees[course] == 0) {
                    q.add(course);
                }
            }
        }

        if(processed.size() == numCourses) {
            return true;
        }

        return false;
    }
}