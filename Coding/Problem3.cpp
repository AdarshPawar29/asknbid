#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	cin>>n;
	int arr[n];
	set<int> s;
	for(int i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	vector<int> v;
	v.push_back(0);
	for(int i=0;i<n;i++)
	{
		v.push_back(v[i]+arr[i]);
	}
	for(int i=1;i<=n;i++)
	{
		for(int j=i;j<=n;j++)
		{
			int k=v[j]-v[i-1];
			s.insert(k);
		}
	}
	cout<<s.size();	
}
