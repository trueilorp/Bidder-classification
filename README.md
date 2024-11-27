# ML Project 
Dataset of about 500 000 rows x 32 colums

To label the Enron email dataset two signals are used to filter suspicious emails and label them into fraud and non-fraud classes:
	- Automated ML labeling:
		Phishing Model Annotation: A high-precision SVM model trained on the Phishing mails dataset, which is used to annotate the Phishing Label on the Enron Dataset.
		Social Engineering Model Annotation: A high-precision SVM model trained on the Social Engineering mails dataset, which is used to annotate the Social Engineering Label on the Enron Dataset.
	
	- Email signals:
		Person Of Interest
		Suspicious Folders
		Sender Type
		Low Communication
		Contains Replies and Forwards
	
	- Manual Inspection: to ensure high-quality labels, the mismatch examples from ML Annotation have been manually inspected for Enron dataset relabeling.