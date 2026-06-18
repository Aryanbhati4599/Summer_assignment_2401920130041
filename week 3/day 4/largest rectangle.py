class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        maxArea = 0
        heights.append(0)  # Sentinel value

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]

                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1

                maxArea = max(maxArea, h * w)

            stack.append(i)

        return maxArea
