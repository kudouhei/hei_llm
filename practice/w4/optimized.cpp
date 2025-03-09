#include <iostream>
#include <vector>
#include <limits>
#include <chrono>
#include <iomanip>

using namespace std;

// LCG function
uint32_t lcg(uint32_t& value, uint32_t a = 1664525, uint32_t c = 1013904223, uint32_t m = 0xFFFFFFFF) {
    value = (a * value + c);
    return value;
}

// Max subarray sum function
long long max_subarray_sum(int n, uint32_t seed, int min_val, int max_val) {
    vector<int> random_numbers(n);
    uint32_t current_seed = seed;
    for (int i = 0; i < n; ++i) {
        random_numbers[i] = lcg(current_seed) % (max_val - min_val + 1) + min_val;
    }

    long long max_sum = numeric_limits<long long>::min();
    for (int i = 0; i < n; ++i) {
        long long current_sum = 0;
        for (int j = i; j < n; ++j) {
            current_sum += random_numbers[j];
            if (current_sum > max_sum) {
                max_sum = current_sum;
            }
        }
    }
    return max_sum;
}

// Total max subarray sum function
long long total_max_subarray_sum(int n, uint32_t initial_seed, int min_val, int max_val) {
    long long total_sum = 0;
    uint32_t seed = initial_seed;
    for (int i = 0; i < 20; ++i) {
        seed = lcg(seed);
        total_sum += max_subarray_sum(n, seed, min_val, max_val);
    }
    return total_sum;
}

int main() {
    int n = 10000;         // Number of random numbers
    uint32_t initial_seed = 42; // Initial seed for the LCG
    int min_val = -10;     // Minimum value of random numbers
    int max_val = 10;      // Maximum value of random numbers

    // Timing the function
    auto start_time = chrono::high_resolution_clock::now();
    long long result = total_max_subarray_sum(n, initial_seed, min_val, max_val);
    auto end_time = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end_time - start_time;

    cout << "Total Maximum Subarray Sum (20 runs): " << result << endl;
    cout << "Execution Time: " << fixed << setprecision(6) << duration.count() << " seconds" << endl;

    return 0;
}
