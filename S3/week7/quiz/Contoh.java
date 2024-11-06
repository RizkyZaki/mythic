public class Contoh{
  public int validField1;
  public String validField2;
  public void printFields(){
    System.out.println("Valid Field 1 " + validField1);
    System.out.println("Valid Field 1 " + validField2);
  }

  public static void main(String[] args) {
    Contoh example = new Contoh();
    example.printFields();
    int localVar;
  }
}