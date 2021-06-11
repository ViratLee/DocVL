import java.security.KeyManagementException;
import java.security.NoSuchAlgorithmException;
import java.security.cert.X509Certificate;

import javax.net.ssl.HostnameVerifier;
import javax.net.ssl.HttpsURLConnection;
import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLSession;
import javax.net.ssl.TrustManager;
import javax.net.ssl.X509TrustManager;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;

import com.aia.cmic.restservices.model.OutputTO;
import com.aia.cmic.restservices.model.UserProfileOutTO;
import com.aia.cmic.restservices.model.UserProfileTO;
import com.aia.cmic.services.helper.Case360Helper;
import com.aia.cmic.services.impl.UAMRestServiceImpl;
import com.fasterxml.jackson.databind.ObjectMapper;

public class TestUAMServiceImpl {
	private static final Logger LOG = LoggerFactory.getLogger(TestUAMServiceImpl.class);
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		disableSslVerification();
		TestUAMServiceImpl uam = new TestUAMServiceImpl();
		//uam.testCallService();
		uam.testCallService2();
	}
	public void testCallService() {
		String restURL = "https://thapi02-uat.aiaazure.biz/uam/rest";
		String url = restURL + "/getUserProfile";
		UserProfileTO userProfileTO = new UserProfileTO();
		userProfileTO.setCompanyCode("051");
		userProfileTO.setSystemId("UAM");
		userProfileTO.setUserId("mpos3a5");
		OutputTO t = null;
		HttpHeaders httpHeaders = new HttpHeaders();
		httpHeaders.setContentType(MediaType.APPLICATION_JSON);
		    try {
		       Case360Helper case360Helper = new Case360Helper();
		       case360Helper.init();
		       ResponseEntity<OutputTO> restResponse = case360Helper.getRestTemplate().exchange(url, HttpMethod.POST,
						new HttpEntity<UserProfileTO>(userProfileTO, httpHeaders), new ParameterizedTypeReference<OutputTO>() {
						});
				
				t = restResponse.getBody();
				ObjectMapper mapper = new ObjectMapper();
			    String jsonString = mapper.writeValueAsString(t);
			    LOG.info(jsonString);
			} catch (Exception e) {
				LOG.error(e.getMessage());
			}
	}
	
	public void testCallService2() {
		String restURL = "https://thapi02-uat.aiaazure.biz/uam/rest";
		String url = restURL + "/getUserProfile";
		UserProfileTO userProfileTO = new UserProfileTO();
		userProfileTO.setCompanyCode("051");
		userProfileTO.setSystemId("UAM");
		userProfileTO.setUserId("bclm022");
		UserProfileOutTO t = null;
		HttpHeaders httpHeaders = new HttpHeaders();
		httpHeaders.setContentType(MediaType.APPLICATION_JSON);
		    try {
		    	Case360Helper case360Helper = new Case360Helper();
		    	case360Helper.init();
		    	ResponseEntity<UserProfileOutTO> postForEntity = case360Helper.getRestTemplate().postForEntity(url, userProfileTO, UserProfileOutTO.class);
		    	//ResponseEntity<UserProfileOutTO> postForEntity = case360Helper.getRestTemplate().postForEntity(url, userProfileTO, UserProfileOutTO.class);
		    	t = postForEntity.getBody();
		    	
				ObjectMapper mapper = new ObjectMapper();
			    String jsonString = mapper.writeValueAsString(t);
			    LOG.info(jsonString);
			} catch (Exception e) {
				LOG.error(e.getMessage());
			}
	}
	
	private static void disableSslVerification() {
		try {
			// Create a trust manager that does not validate certificate chains
			TrustManager[] trustAllCerts = new TrustManager[] { new X509TrustManager() {
				public java.security.cert.X509Certificate[] getAcceptedIssuers() {
					return null;
				}
	
				public void checkClientTrusted(X509Certificate[] certs, String authType) {
				}
	
				public void checkServerTrusted(X509Certificate[] certs, String authType) {
				}
			} };
	
			// Install the all-trusting trust manager
			SSLContext sc = SSLContext.getInstance("SSL");
			sc.init(null, trustAllCerts, new java.security.SecureRandom());
			HttpsURLConnection.setDefaultSSLSocketFactory(sc.getSocketFactory());
	
			// Create all-trusting host name verifier
			HostnameVerifier allHostsValid = new HostnameVerifier() {
				public boolean verify(String hostname, SSLSession session) {
					return true;
				}
			};
	
			// Install the all-trusting host verifier
			HttpsURLConnection.setDefaultHostnameVerifier(allHostsValid);
		} catch (NoSuchAlgorithmException e) {
			e.printStackTrace();
		} catch (KeyManagementException e) {
			e.printStackTrace();
		}
	}
}
