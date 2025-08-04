class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        lst=[]
        for i in range(len(image)):
            img=image[i][::-1]
            for j in range(len(img)):
                if img[j]==0:
                    img[j]=1
                elif img[j]==1:
                    img[j]=0
            lst.append(img)
        return lst

        