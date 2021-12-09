# python 과 javascript는 overloading 함수를 지원하지 않기 때문에 Java 예시

# public class Math {
  
#     public int sum(int x, int y)
#     {
#         return (x + y);
#     }
  
#     public int sum(int x, int y, int z)
#     {
#         return (x + y + z);
#     }
  
#     public double sum(double x, double y)
#     {
#         return (x + y);
#     }
  
#     public static void main(String args[])
#     {
#         Math math = new Math();
#         System.out.println(math.sum(1, 2));
#         System.out.println(math.sum(3, 4, 5));
#         System.out.println(math.sum(7.7, 8.8));
#     }
# }