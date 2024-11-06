
public class Travel {
    public static final int INDIVIDUAL = 0;
    public static final int PACKAGE = 1;

    private String travelCode;
    private String cityName;
    private String flight;
    private int travelType;
    private int maxPeople;
    private int resvPeople;

    public Travel(String travelCode, String cityName, String flight, int travelType, int maxPeople) {
        this.travelCode = travelCode;
        this.cityName = cityName;
        this.flight = flight;
        this.travelType = travelType;
        this.maxPeople = maxPeople;
        this.resvPeople = 0;
    }

    public String getTravelCode() {
        return travelCode;
    }

    public int getTravelType() {
        return travelType;
    }

    public int getMaxPeople() {
        return maxPeople;
    }

    public int getResvPeople() {
        return resvPeople;
    }

    public void setMaxPeople(int maxPeople) {
        if (maxPeople < this.resvPeople) {
            System.out.println("[Info] Jumlah maksimum reservasi disesuaikan dengan jumlah reservasi saat ini.");
            this.maxPeople = this.resvPeople;
        } else {
            this.maxPeople = maxPeople;
        }
    }

    public void setResvPeople(int resvPeople) {
        if (resvPeople > this.maxPeople) {
            System.out.println("[Error] Jumlah peserta tidak boleh melebihi jumlah maksimal reservasi (" + this.maxPeople + " orang).");
        } else {
            this.resvPeople = resvPeople;
        }
    }

    public void printTravelInfo() {
        String type = (travelType == INDIVIDUAL) ? "Individu" : "Paket";
        String status = (resvPeople == 0) ? "-" : (resvPeople >= maxPeople ? "Sold out" : "");
        System.out.printf("%-12s %-12s %-15s %-10s %-15s %-15s %-10s%n", travelCode, cityName, flight, type, maxPeople + " orang", resvPeople + " orang", status);
    }
}