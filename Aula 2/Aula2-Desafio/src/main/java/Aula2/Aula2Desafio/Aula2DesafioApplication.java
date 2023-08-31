package Aula2.Aula2Desafio;

import java.io.FileWriter;
import java.io.IOException;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Aula2DesafioApplication {

	public static void main(String[] args) throws IOException{
		SpringApplication.run(Aula2DesafioApplication.class, args);
		
		Document doc = Jsoup.connect("https://pt.wikipedia.org/wiki/Fórmula_1").get();
		FileWriter file = new FileWriter("site.txt");

		file.write(doc.getElementsByTag("h1").toString());
		file.write(doc.getElementsByTag("h2").toString());
		file.close();
	}

}
