# PRIVAFRAME
Script to run PRIVAFRAME on FRED and analyze your sensitive data

The python script can be executed in order to analyze your sentitive data.

- You have to replace the .csv filename with the dataset you want to analyze.
- The dataset will be analyzed by a FRED API and frames will be detected.
- The frame-based analysis will be matched with the PRIVAFRAME knowledge and a new file labeled with sensitive Personal Data Categories will be created.

A test-set used as model evaluation is attached. The test-set is composed of 3671 sentence with a multi-labels Personal Data Categories annotation. The PRIVAFRAME evaluation test achieved a 77% of accuracy.

# Instructions for downloading PRIVAFRAME

To download the py code and the dataset you have to sign an agreement of ethical research purposes. You can find the agreement doc in this repository.

Once the corresponding license agreement is signed, you have to send it to gaia.gambarelli2@unibo.it.

Subject: [PRIVAFRAME download]

Body: Your name, e-mail, telephone number, organization, postal mail, purpose for which you will use the model, time and date at which you sent the email with the signed license agreement.

Attachments: the document of agreement signed for the parts of the licensee.

Once the email copy of the license agreement has been received, you will receive the PRIVAFRAME code and the labeled dataset.

For additional informations, please contact the authors.

