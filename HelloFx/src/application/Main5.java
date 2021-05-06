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

	
public class Main5 extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = FXMLLoader.load(getClass().getResource("main5.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();	
			
			Button btn = (Button) scene.lookup("#btn");
			TextField tfMine	= (TextField) scene.lookup("#tfMine");
			TextField tfCom		= (TextField) scene.lookup("#tfCom");
			TextField tfResult	= (TextField) scene.lookup("#tfResult");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					String mine	= tfMine.getText();
					String com	= "";
					String result = "";
					double rnd = Math.random();
					if(rnd > 0.5) {
						com = "홀";
					}else {
						com = "짝";
					}
					tfCom.setText(com);
					
					if(mine.equals(com)) {
						result = "같습니다.";
					}else {
						result = "다릅니다.";
					}
					tfResult.setText(result);
					
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
