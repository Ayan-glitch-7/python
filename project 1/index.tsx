

        setResults(data);
        toast.success("Analysis complete!");
        setIsAnalyzing(false);
      };
    } catch (error) {
      console.error('Error:', error);
      toast.error("An error occurred. Please try again.");
      setIsAnalyzing(false);
    }
  };

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section 
        className="relative py-24 px-6 bg-gradient-to-b from-background to-primary/5"
        style={{
          backgroundImage: `linear-gradient(rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.95)), url(${heroBg})`,
          backgroundSize: 'cover',
          backgroundPosition: 'center'
        }}
      >
        <div className="container mx-auto max-w-6xl text-center">
          <div className="inline-flex items-center gap-2 px-4 py-2 bg-primary/10 rounded-full mb-6 border border-primary/20">
            <Sparkles className="h-4 w-4 text-primary" />
            <span className="text-sm font-medium text-primary">AI-Powered Health Analysis</span>
          </div>
          
          <h1 className="text-5xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
            Your Face, Your Health
          </h1>
          
          <p className="text-xl text-muted-foreground mb-12 max-w-3xl mx-auto">
            Upload your photo and receive personalized health insights, risk assessments, 
            and actionable recommendations powered by advanced AI technology.
          </p>
        </div>
      </section>

      {/* Upload Section */}
      <section className="py-16 px-6">
        <div className="container mx-auto max-w-4xl">
          <ImageUpload 
            onImageSelect={setSelectedImage} 
            selectedImage={selectedImage}
          />
          
          {selectedImage && !results && (
            <div className="mt-8 text-center">
              <Button 
                size="lg"
                onClick={handleAnalyze}
                disabled={isAnalyzing}
                className="px-12 py-6 text-lg"
              >
                {isAnalyzing ? (
                  <>
                    <Loader2 className="mr-2 h-5 w-5 animate-spin" />
                    Analyzing...
                  </>
                ) : (
                  <>
                    <Sparkles className="mr-2 h-5 w-5" />
                    Analyze My Health
                  </>
                )}
              </Button>
            </div>
          )}
        </div>
      </section>

      {/* Results Section */}
      {results && (
        <section className="py-16 px-6 bg-muted/30">
          <div className="container mx-auto max-w-6xl">
            <h2 className="text-4xl font-bold text-center mb-12">
              Your Health Analysis
            </h2>
            <AnalysisResults
              healthRisks={results.healthRisks || []}
              currentConditions={results.currentConditions || []}
              dietPlan={results.dietPlan || []}
              medicalAdvice={results.medicalAdvice || []}
            />
            
            <div className="mt-12 text-center">
              <Button 
                variant="outline" 
                size="lg"
                onClick={() => {
                  setResults(null);
                  setSelectedImage(null);
                }}
              >
                Analyze Another Photo
              </Button>
            </div>
          </div>
        </section>
      )}
    </div>
  );
};

export default Index;
