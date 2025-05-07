class Solution {
public:
    int busyStudent(vector<int>& startTime, vector<int>& endTime, int queryTime) {
        // Step 1: Create a timeline array to track student activity.
        vector<int> time(1005, 0);  // Array to handle times up to 1000.

        // Step 2: Update the timeline array for each student's start and end time.
        for (int x : startTime) {
            time[x]++;  // Increment at the start time.
        }
        for (int x : endTime) {
            time[x + 1]--;  // Decrement at one past the end time.
        }

        // Step 3: Build the prefix sum to calculate the number of active students at each time.
        for (int i = 1; i < time.size(); ++i) {
            time[i] += time[i - 1];  // Add the previous time's value.
        }

        // Step 4: Return the number of students active at the query time.
        return time[queryTime];
    }
};