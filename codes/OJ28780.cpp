#include <cstdio>
using namespace std;
int main(void)
{
	int n, m;
	scanf("%d %d", &n, &m);
	int *coins = new int[n];
	int *dp = new int[m+1];
	for(int i = 0; i < n; i++)
	{
		scanf("%d", &coins[i]);
		if(coins[i] <= m+1)
			dp[coins[i]] = 1;
	}
	for(int i = 0; i < n; i++)
		for(int j = 1 + coins[i]; j < m+1; j++)
		{
			if(dp[j-coins[i]] != 0)
				if(dp[j] == 0)
					dp[j] = dp[j-coins[i]] + 1;
				else
					dp[j] = dp[j] < dp[j-coins[i]]+1 ? dp[j] : dp[j-coins[i]] + 1;
		}
	if(dp[m] == 0)			
		printf("-1");
	else
		printf("%d\n", dp[m]);
	delete[] coins;
	delete[] dp;			
}