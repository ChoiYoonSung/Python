package day03;

public class OopTest {
	public static void main(String[] args) {
		Human hum = new Human();
		System.out.println(hum.fullness);
		System.out.println(hum.flag_cook);
		hum.eat();
		System.out.println(hum.fullness);
		hum.full();
		hum.goHakwon();
		System.out.println(hum.fullness);
		System.out.println(hum.flag_cook);
	}
}