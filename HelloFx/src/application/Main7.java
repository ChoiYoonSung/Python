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

	
public class Main7 extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = FXMLLoader.load(getClass().getResource("main7.fxml"));
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
					if(rnd <= 0.33) {
						com = "가위";
					}else if(rnd > 0.33 && rnd <= 0.66){
						com = "바위";
					}else {
						com = "보";
					}
					
					if(mine.equals("가위")) {
						if(com.equals("가위")) {
							result = "비겼습니다.";
						}else if(com.equals("바위")) {
							result = "졌습니다.";
						}else{
							result = "이겼습니다.";
						}
					}else if(mine.equals("바위")) {
						if(com.equals("가위")) {
							result = "이겼습니다.";
						}else if(com.equals("바위")) {
							result = "비겼습니다.";
						}else{
							result = "졌습니다.";
						}
					}else if(mine.equals("보")){
						if(com.equals("가위")) {
							result = "졌습니다.";
						}else if(com.equals("바위")) {
							result = "이겼습니다.";
						}else{
							result = "비겼습니다.";
						}
					}else {
						result = "잘못된 입력입니다.";
					}
					tfCom.setText(com);
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
