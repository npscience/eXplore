Lens Fork for 'eXplore' project, HackCambridge 2017
========

We used the eLife Lens project in order to make tutorials for personal genetics that are a bit more personal!

For example, rather than reading a static article about how genetics influences taste preferences, we wanted to generate a dynamic article based on the user's own genetic data (e.g. through 23andMe).

What is implemented now:
- Lens fork with example 'taste_prefs.xml' for a specific person's genotype.

What we still want to work on:
- Dynamic xml generation based on user 23andMe data

# Getting Started

Be sure to install node.js which is used to run the code. Once you have node.js installed:

1. Clone the repository (feel free to fork and play around!)
```bash
git clone https://github.com/pjshort/eXplore
```

2. Install any dependencies
```bash
cd eXplore
cd lens-explore
npm install
```
3. Run the server (visible on http://127.0.0.1:4001/)

```bash
node server.js
```

The taste preferences article will display on port 4001 (http://127.0.0.1:4001/)
