#include <bits/stdc++.h>

using namespace std;

int ans = 0;

int main(void)
{
  cin.tie(NULL);
  ios::sync_with_stdio(false);

  while (!cin.eof() && cin.good())
  {
    string s;
    cin >> s;

    stack<char> braket;

    int len = s.length();
    char illegal_braket = '0';

    if (len == 0)
      break;

    for (int i = 0; i < len; i++)
    {
      if (s[i] == '(' || s[i] == '[' || s[i] == '{' || s[i] == '<')
        braket.push(s[i]);

      else if (s[i] == ')')
      {
        if (!braket.empty())
        {
          if (braket.top() == '(')
            braket.pop();

          else
          {
            illegal_braket = s[i];
            break;
          }
        }
      }

      else if (s[i] == ']')
      {
        if (!braket.empty())
        {
          if (braket.top() == '[')
            braket.pop();

          else
          {
            illegal_braket = s[i];
            break;
          }
        }
      }

      else if (s[i] == '}')
      {
        if (!braket.empty())
        {
          if (braket.top() == '{')
            braket.pop();

          else
          {
            illegal_braket = s[i];
            break;
          }
        }
      }

      else if (s[i] == '>')
      {
        if (!braket.empty())
        {
          if (braket.top() == '<')
            braket.pop();

          else
          {
            illegal_braket = s[i];
            break;
          }
        }
      }
    }

    if (illegal_braket == ')')
      ans += 3;

    else if (illegal_braket == ']')
      ans += 57;

    else if (illegal_braket == '}')
      ans += 1197;

    else if (illegal_braket == '>')
      ans += 25137;
  }

  cout << ans;

  return 0;
}