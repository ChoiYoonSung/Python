package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

	
public class Main4 extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = FXMLLoader.load(getClass().getResource("main4.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			Button btn = (Button) scene.lookup("#btn");
			TextField tf1 = (TextField) scene.lookup("#tf1");
			TextField tf2 = (TextField) scene.lookup("#tf2");
			TextField tf3 = (TextField) scene.lookup("#tf3");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					int a1 = Integer.parseInt(tf1.getText());
					int a2 = Integer.parseInt(tf2.getText());
					int a3 = 0;
					for(int i = a1; i <= a2; i++) {
						a3 += i;
					}
					tf3.setText(a3 + "");
				}
				
			});
			
		} catch(Exception e) {
			e.printStackTrace();
		}
		
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
