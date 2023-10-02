#include <bits/stdc++.h>

using namespace std;

int main()
{
    string s;
    cin >> s;
    int cntL = 0;
    int cntR = 0;

    string current_sstr = "";
    int cnt_blance = 0;

    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == 'L')
        {
            cntL++;
        }
        else
        {
            cntR++;
        }

        if (cntL == cntR)
        {
            cnt_blance++;
            current_sstr = "";
        }
    }
    cout << cnt_blance << endl;

    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == 'L')
        {
            cntL++;
        }
        else
        {
            cntR++;
        }

        current_sstr += s[i];

        if (cntL == cntR)
        {
            cnt_blance++;
            cout << current_sstr << endl;
            current_sstr = "";
        }
    }
    return 0;
}