#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int a[n];
    int cnt = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    while (true)
    {
        bool even = true;
        for (int i = 0; i < n; i++)
        {
            if (a[i] % 2 != 0)
            {
                even = false;
                break;
            }
            a[i] /= 2;
        }
        if (even)
        {
            cnt++;
        }
        else
        {
            break;
        }
    }

    cout << cnt;
    return 0;
}