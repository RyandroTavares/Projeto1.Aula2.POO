package Aula2.Aula2java;

import java.io.IOException;


import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Aula2JavaApplication {

	public static void main(String[] args) throws IOException{
		SpringApplication.run(Aula2JavaApplication.class, args);

		Document doc = Jsoup.connect("https://pt.wikipedia.org/wiki/Fórmula_1").get();
		System.out.println(doc);
		System.out.println(doc.getElementsByTag("p"));
		System.out.println(doc.getElementsContainingOwnText("o verde para as equipes inglesas, "));
	}

}
