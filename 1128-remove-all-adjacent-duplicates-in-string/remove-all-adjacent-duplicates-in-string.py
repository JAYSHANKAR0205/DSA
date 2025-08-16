class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[]
        top=-1
        for i in range(len(s)):
            if top>=0 and st[top]==s[i]:
                st.pop()
                top-=1
            else:
                st.append(s[i])
                top=top+1
        s1=""
        for i in st:
            s1=s1+i
        return s1

        


        