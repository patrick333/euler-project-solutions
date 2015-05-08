//Lexicographic permutations


static void Main(string[] args)
{
char[] testC = new char[] { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
//Array.Reverse(testC);
////testC=testC.Reverse().ToArray();  //two methods for reverse. 
//nextP(ref testC);
//foreach (var c in testC)
//{
//    Console.Write(c);
//}

for (int i = 1; i <=1000000 - 1; i++)
{
    if (!nextP(ref testC))
    {
        Console.Write("Will break.");
        break;
    }
    if (i % 100==0)
    {
        foreach (var c in testC)
        {
            Console.Write(c);
        }
        Console.Write(' ');
    }
}

foreach (var c in testC)
{
    Console.Write(c);
}
}//end of Main()