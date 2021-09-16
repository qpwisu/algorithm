#3 max subarray  내가 푼거 산날과 판날을 알 수 있음 튜플을 이용



#include <string>
#include <vector>
#include <climits>
#include <iostream>
#include <tuple>
#include <cmath>
    using namespace std;


    tuple<int, int, int> findcrosssub(vector<int> & A, int low, int mid, int high) {
        int leftsum = -INT_MAX;
        int sum = 0;
        int maxleft = 0;
        int maxright = 0;
        for (int i = mid; i >= low; i--) {
            sum = sum + int(A[i]);
            if (sum > leftsum) {
                leftsum = sum;
                maxleft = i;

            }
        }
        int rightsum = -INT_MAX;
        sum = 0;
        for (int j = mid + 1; j <= high; j++) {
            sum = sum + int(A[j]);
            if (sum > rightsum) {

                rightsum = sum;
                maxright = j;

            }
        }

        return make_tuple(maxleft, maxright, leftsum + rightsum);

    }


    tuple<int, int, int> findmaxsub(vector<int> & A, int low, int high) {

        if (high == low) {

            return make_tuple(low, high, A[low]);
        }
        else {
            int mid = floor((low + high) / 2);
            tuple<int, int, int> a = findmaxsub(A, low, mid);
            int leftlow = get<0>(a);
            int lefthigh = get<1>(a);
            int leftsum = get<2>(a);

            int mid2 = mid + 1;
            tuple<int, int, int>  b = findmaxsub(A, mid2, high);
            int rightlow = get<0>(b);
            int righthigh = get<1>(b);
            int rightsum = get<2>(b);

            tuple<int, int, int>  c = findcrosssub(A, low, mid, high);
            int crosslow = get<0>(c);
            int crosshigh = get<1>(c);
            int crosssum = get<2>(c);
            if (leftsum >= rightsum && leftsum >= crosssum) {
                return make_tuple(leftlow, lefthigh, leftsum);
            }
            else if (rightsum >= leftsum && rightsum >= crosssum) {
                return make_tuple(rightlow, righthigh, rightsum);
            }
            else {
                return make_tuple(crosslow, crosshigh, crosssum);

            }


        }

    }





    int solution(vector<int> param0) {
        int answer = 0;
        int low = 0;
        int high = param0.size() - 1;
        tuple<int, int, int>  a = findmaxsub(param0, low, high);
        answer = get<2>(a); // 여기서 get에 0을 넣으면 산 날 index 1을 넣으면 판날 index 2는 산날과 판날의 가격차

        return answer;
    }




    int main() {
        int aa[] = { 13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7 };

        vector<int> a(aa, aa + sizeof(aa) / sizeof(aa[0]));
        int answer = solution(a);
        cout << answer << endl;

    }





#include <string>
#include <vector>
#include <climits>
#include <iostream>

    using namespace std;

    int find_max_crossing_subarray(vector<int> & A, int low, int mid, int high);
    int find_maximum_subarray(vector<int> & A, int low, int high) {
        if (low == high) {
            return A[low];
        }
        else {
            int mid = (low + high) / 2;
            int leftSum = find_maximum_subarray(A, low, mid);
            int rightSum = find_maximum_subarray(A, mid + 1, high);
            int crossSum = find_max_crossing_subarray(A, low, mid, high);
            if (leftSum >= rightSum && leftSum >= crossSum) {
                return (leftSum);
            }
            else if (rightSum >= leftSum && rightSum >= crossSum) {
                return (rightSum);
            }
            else {
                return (crossSum);
            }
        }
    }
    int find_max_crossing_subarray(vector<int> & A, int low, int mid, int high) {
        int leftSum = INT_MIN;
        int sum = 0;
        for (int i = mid; i >= low; i--) {
            sum += A[i];
            if (sum > leftSum) {
                leftSum = sum;
            }
        }
        int rightSum = INT_MIN;
        sum = 0;
        for (int j = mid + 1; j <= high; j++) {
            sum += A[j];
            if (sum > rightSum) {
                rightSum = sum;
            }
        }
        return leftSum + rightSum;
    }
    int solution(vector<int> param0) {

        int low = 0;
        int high = param0.size() - 1;
        auto a = find_maximum_subarray(param0, low, high);
        int answer = a;

        return answer;
    }
    int main() {
        int aa[] = { 13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7 };
        vector<int> a(aa, aa + 16);
        int answer = solution(a);
        cout << answer << endl;
    }


