#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        vector<int> a(n);
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }

        // Sort the input array in ascending order
        // sort(a.begin(), a.end());

        // Find the minimum value of bn by iterating from 1 to n
        int min_bn = 1;
        for (int i = 0; i < n; i++)
        {
            if (a[i] > min_bn)
            {
                min_bn = a[i] + 1;
            }
        }

        cout << min_bn << endl;
    }

    return 0;
}
