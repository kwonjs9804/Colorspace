using System;

class Person
{
    public String? Name;
    public String? Birthday;
    public String? Hobby;

    public void Eat()
    {
        Console.WriteLine(Name + "(이)가 아침을 먹습니다.");
    }
    public void Day()
    {
        Console.WriteLine(Birthday + "(은)는 " + Name + "(이)의 생일입니다.");
    }
    public void Play()
    {
        Console.WriteLine(Name + "(이)의 취미는 " + Hobby + " 입니다.");
    }
}
class MainClass
{
    public static void Main(string[] args)
    {
        Person p1;
        p1 = new Person();
        p1.Name = "준석";
        p1.Birthday = "04.24";
        p1.Hobby = "게임";

        p1.Eat();
        p1.Day();
        p1.Play();
    }
}